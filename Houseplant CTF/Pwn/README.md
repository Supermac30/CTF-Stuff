# pwn

## Pie Generator
The fatal mistake of this developer was setting the seed on the clientside. The timestamp of when we press submit is sent as the seed and the value as our guess. In firefox, solving this problem is as simple as going into the network tab after guessing, resubmitting our request, and changing the guess while keeping the timestamp constant.

Flag: rtcp{w0w_sO_p53uD0}