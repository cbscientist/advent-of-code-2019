from math import ceil
import time

start_time = time.clock()
input_number = "59715091976660977847686180472178988274868874248912891927881770506416128667679122958792624406231072013221126623881489317912309763385182133601840446469164152094801911846572235367585363091944153574934709408511688568362508877043643569519630950836699246046286262479407806494008328068607275931633094949344281398150800187971317684501113191184838118850287189830872128812188237680673513745269645219228183633986701871488467284716433953663498444829748364402022393727938781357664034739772457855166471802886565257858813291667525635001823584650420815316132943869499800374997777130755842319153463895364409226260937941771665247483191282218355610246363741092810592458"
# input_number = '12345678'  # 0.008445000000000008
multiplication_factor = ceil(len(input_number) / 4)

base_pattern = [0, 1, 0, -1]

num_phases = 100

for phase in range(num_phases):
    output_number = ""
    for index, digit in enumerate(input_number):
        position = index + 1
        pattern = [[pattern_element] * position for pattern_element in base_pattern]
        pattern = [element for sublist in pattern for element in sublist]
        pattern = pattern * multiplication_factor
        pattern = pattern[1 : len(pattern)] + [pattern[0]]
        pattern = pattern[0 : len(input_number)]
        output_value = abs(
            sum([int(item[0]) * int(item[1]) for item in zip(input_number, pattern)])
        )
        new_digit = str(output_value)[len(str(output_value)) - 1]  # rightmost digit
        output_number += new_digit
    input_number = output_number

end_time = time.clock()
print(output_number)
print((end_time - start_time))
