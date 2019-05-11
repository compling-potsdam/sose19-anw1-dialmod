# coding: utf-8

from __future__ import division, print_function
import json
import argparse


def strict_compare(pred_sem, gold_sem):
    matching = True
    for da_pred, da_gold in zip(pred_sem, gold_sem):
        if da_pred['slots'] != da_gold['slots'] or da_pred['act'] != da_gold['act']:
            matching = False
    return (1, None) if matching else (0, None)


def any_order(func, pred_sem, gold_sem):
    res, _ = func(pred_sem, gold_sem)
    if res == 0 and len(gold_sem) > 1:
        # this is a bit hacky. makes assumption that there are at most
        # two intents per utterance.. if match didn't work with one order,
        # try again with order reversed
        res, _ = func(pred_sem, gold_sem[::-1])
    return (res, None)


def slot_set(sem):
    return set([tuple(slot) for act in sem for slot in act['slots']])


def ser(pred_sem, gold_sem):
    pred_slots = slot_set(pred_sem)
    gold_slots = slot_set(gold_sem)
    # this is not quite correct. Typically, SER would be calculated
    # based on positions / spans over the string.
    # I'm not doing this here, so I don't compute substitutions
    inserted = len(pred_slots - gold_slots)
    deleted = len(gold_slots - pred_slots)
    return 0 if len(gold_slots) == 0 else (inserted + deleted) / len(gold_slots)


def tpfpfn(pred_sem, gold_sem):
    pred_slots = slot_set(pred_sem)
    gold_slots = slot_set(gold_sem)

    tp = len(pred_slots.intersection(gold_slots))
    fp = len(pred_slots - gold_slots)
    fn = len(gold_slots - pred_slots)
    return tp, fp, fn


def eval_nlu(injson, goldjson):

    out = []

    correct = 0
    tp = fp = fn = 0
    ser_acc = 0

    # this is assuming that they are in same order
    # you could also go by IDs and evaluate only those
    # turns which are both in predicted and gold
    for n, (pred, gold) in enumerate(zip(predicted_data, gold_data)):
        dial_id = pred['dial_id']
        turn_id = pred['turn_id']
        utt = pred['usr_utt']

        pred_sem = pred['usr_sem']
        gold_sem = gold['usr_sem']
        
        #print('=' * 20)
        #print(json.dumps(pred_sem, indent=2))
        #print('-' * 20)
        #print(json.dumps(gold_sem, indent=2))
        
        # now compare them in some way
        #  this is the strictest, and least informative way:
        score, _ = any_order(strict_compare, pred_sem, gold_sem)
        correct += score
        
        slot_error_rate = ser(pred_sem, gold_sem)
        ser_acc += slot_error_rate

        this_tp, this_fp, this_fn = tpfpfn(pred_sem, gold_sem)
        tp += this_tp
        fp += this_fp
        fn += this_fn

        out.append({'dial_id': dial_id,
                    'turn_id': turn_id,
                    'usr_utt': utt,
                    'errors': 'I DO NOT MAKE ERRORS'})

    print('Full Frame Accuracy: {:.4f}'.format(correct / n))
    print('Slot Error Rate: {:.4f}'.format(ser_acc / n))
    prec = tp / (tp + fp)
    rec = tp / (tp + fn)
    print('Precision: {:.4f}'.format(prec))
    print('   Recall: {:.4f}'.format(rec))
    print('       F1: {:.4f}'.format(2 * (prec * rec) / (prec + rec)))
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Evaluate NLU component')
    parser.add_argument('input',
                        help='the file with the predictions')
    parser.add_argument('gold',
                        help='the respective gold standard info')
    parser.add_argument('errorlog',
                        help='where to write info about errors')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        predicted_data = json.load(f)
    with open(args.gold, 'r') as f:
        gold_data = json.load(f)

    out = eval_nlu(predicted_data, gold_data)

    with open(args.errorlog, 'w') as f:
        json.dump(out, f, indent=2)
