import test from 'node:test';
import assert from 'node:assert/strict';
import { attemptDelivery as original } from '../samples/retry-budget-original.mjs';
import { attemptDelivery as repair } from '../samples/retry-budget-repair.mjs';
import { showHints as originalHints } from '../samples/explicit-false-original.ts';
import { showHints as repairedHints } from '../samples/explicit-false-repair.ts';
test('retry budget counterexamples and early success', () => {
  assert.equal(original(0, () => false), 1);
  assert.equal(repair(0, () => false), 0);
  assert.equal(original(3, () => false), 4);
  assert.equal(repair(3, () => false), 3);
  assert.equal(repair(3, () => true), 1);
});
test('explicit false survives the repaired default', () => {
  assert.equal(originalHints({showHints:false}), true);
  assert.equal(repairedHints({showHints:false}), false);
  assert.equal(repairedHints({showHints:true}), true);
  assert.equal(repairedHints({}), true);
});
