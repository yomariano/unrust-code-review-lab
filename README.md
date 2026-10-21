# Unrust code review lab

Three original, public code review challenges with written contracts, counterexamples, explanations and runnable checks. Read the contract and predict the original behavior before opening the repair.

| Challenge | Contract | Worked explanation |
| --- | --- | --- |
| JavaScript retry budget | The total call budget includes the first attempt. Zero means zero calls. | [Trace the retry loop](https://unrust.dev/guides/javascript-retry-budget-challenge) |
| Python iterator consumption | A list and one-shot generator with the same rows must produce the same total. | [Review the iterator](https://unrust.dev/guides/python-iterator-consumption-challenge) |
| TypeScript explicit false | Omission defaults to true; explicit false must stay false. | [Inspect the default](https://unrust.dev/guides/typescript-explicit-false-challenge) |

## Run the checks

Use Node.js 22.18 or later and Python 3. There are no third-party dependencies. Node’s built-in type stripping executes the actual TypeScript source; it does not type-check it.

```sh
git clone https://github.com/yomariano/unrust-code-review-lab.git
cd unrust-code-review-lab
npm test
```

The tests intentionally demonstrate failures in each original and verify repairs against the stated examples. A passing check establishes these cases, not production reliability or a skill score. The retry snippet omits production concerns such as backoff and idempotency. The Python input is finite and schema-valid. The TypeScript type does not validate untrusted JSON.

## Use it in a team or tutorial

1. State the contract and show the original snippet.
2. Ask for a predicted result and the smallest counterexample.
3. Compare with the explanation, then run the checks.
4. Add one new case and state what it establishes.

The full teaching pack is in [teaching-pack.json](./teaching-pack.json). These MIT-licensed examples were authored for Unrust and checked on 21 October 2026. They are separate from the diagnostic and Daily puzzle banks, contain no assessment answers and produce no diagnostic score.

[Explore the public lab](https://unrust.dev/guides/public-code-review-challenges) · [Unrust](https://unrust.dev) · [Mariano on X](https://x.com/yomariano05)
