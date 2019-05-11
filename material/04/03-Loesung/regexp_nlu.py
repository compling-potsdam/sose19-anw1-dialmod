# coding: utf-8

import json
import argparse
import re


def nlu(data, grammar):

    out = []

    # TODO: pre-compile slot res

    for turn in data:
        dial_id = turn['dial_id']
        turn_id = turn['turn_id']
        utt = turn['usr_utt']

        usr_sem = []

        # go through the intents, try to match their regexps
        for intent_name, rules in grammar['intents']:
            match = re.search(rules['regexp'], utt)

            # I have matched an intent!
            if match:
                intent_span = match.span()

                # now looking for this intent's obligatory slots
                out_slots = []
                for slot in rules['slots']:
                    # this should be pre-compiled once outside of the loop...
                    slot_re = '|'.join(grammar['slots'][slot])
                    match = re.search(slot_re, utt)
                    if match:
                        out_slots.append((slot, match.group(), match.span()))

                # if you should have matched a slot, but didn't,
                # break out and try next intent
                if len(rules['slots']) != 0 and len(out_slots) == 0:
                    continue
                else:
                    if len(out_slots) == 0:
                        out_slots = [(None, None, None)]
                    for slot, value, slot_span in out_slots:
                        usr_sem.append({
                            'act': intent_name,
                            'act_span': intent_span,
                            'slots': [
                                [slot, value]
                            ] if slot is not None else [],
                            'slot_span': slot_span
                        })

        # if we don't have anything yet, try those intents where the
        # slot can be matched without any surrounding context
        if len(usr_sem) == 0:
            out_slots = []
            for nm_intent_name in grammar['no-match-intents']:
                # for these intents, use the slots without the intent
                # context rules
                # this should probably be a function, as this is
                # pretty much the same code as above..
                for intent_name, rules in grammar['intents']:
                    if intent_name != nm_intent_name:
                        continue
                    for slot in rules['slots']:
                        slot_re = '|'.join(grammar['slots'][slot])
                        match = re.search(slot_re, utt)
                        if match:
                            out_slots.append((slot, match.group(), match.span()))
                    if len(out_slots) == 0:
                        continue
                    else:
                        for slot, value, slot_span in out_slots:
                            usr_sem.append({
                                'act': intent_name,
                                'act_span': (0, 0),
                                'slots': [
                                    [slot, value]
                                ],
                                'slot_span': slot_span
                            })
                        break
                # here we only try to match one intent;
                # if we've found something, we break out of loop
                if len(usr_sem) != 0:
                    break

        out.append({'dial_id': dial_id,
                    'turn_id': turn_id,
                    'usr_utt': utt,
                    'usr_sem': usr_sem})

    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='RegExp-based NLU component')
    parser.add_argument('input',
                        help='the JSON file with the utterances')
    parser.add_argument('output',
                        help='where to write the output with the DAs added')
    parser.add_argument('-g', '--grammar',
                        default='grammar.json',
                        help='the regexp grammar to use')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        data = json.load(f)

    with open(args.grammar, 'r') as f:
        grammar = json.load(f)

    outjson = nlu(data, grammar)

    with open(args.output, 'w') as f:
        json.dump(outjson, f, indent=2)
