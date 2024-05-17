def main():
    sequence = 'AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG'
    for subsequence in ['AGATC', 'AATG', 'TATC']:
        print(f'Longest match for subsequence {subsequence} is: {longest_match(sequence, subsequence)}')


def longest_match(sequence, subsequence):
    longest_run = 0
    sequence_length = len(sequence)
    subsequence_length = len(subsequence)

    for i in range(sequence_length):
        count = 0
        
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)
    return longest_run


main()
