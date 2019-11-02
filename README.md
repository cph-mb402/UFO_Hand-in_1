# UFO_Hand-in_1

## Queries and pages

The queries we have used to try and solve the problem of decoding the hidden message can be found in the Browsing History.txt file

## Stumbles

In solving our problem, we started off by just trying to get the red channel data and get the LSB (Least Significant Bit). Once we got a list of those, we then separated them into bytes and tried decoding them into their ascii character with the chr method from python. Unfortunately it seems that the final string we decode is far from readable, and our assumption is wrong somewhere.

The biggest struggles we had was in deciding how to get the LSB from the red channel, how to link the bits together into bytes (we ended up going with a string approach, but also tried list and bytearray before), and, finally, getting a correct decoding.

Although we went back on all 3 aspects of the implementation, trying to figure out our fault, we haven't come up with a working solution, and we aren't sure if it's a technical mistake in the way we coded it, or if it's one of our assumptions of how the message was encoded in the first place that did not allow us to come to a correct answer.

## Diary

Entry 1:
Started by creating a repository and a document to write progress into. Initial research on the topic of stenography and what kind of technical challanges we are to expect. Discussion in group to plan our approach to the solution

Entry 2:
Started coding the project, getting our first outputs.

Entry 3:
More research in regards to how LSB is found in stenography, encoding and decoding the bits to bytes.

Entry 4:
Continued changing implementations while researching. We have arrived at working solutions that decode the bytes we have collected, but unfortunately still do not produce any readable strings.