def counting_sort(words, max_len):
  """
  단어 리스트를 길이와 사전 순으로 정렬하는 함수입니다.

  Args:
    words: 정렬할 단어 리스트
    max_len: 단어의 최대 길이

  Returns:
    정렬된 단어 리스트
  """
  buckets = [[] for _ in range(max_len + 1)]
  for word in words:
    buckets[len(word)].append(word)

  sorted_words = []
  for i in range(max_len + 1):
    bucket = buckets[i]
    for j in range(len(bucket)):
      for k in range(j):
        if _compare_words(bucket[j], bucket[k]):
          bucket[j], bucket[k] = bucket[k], bucket[j]
    sorted_words.extend(bucket)

  return sorted_words

def _compare_words(word1, word2):
  """
  두 단어를 철자 하나씩 비교하는 함수입니다.

  Args:
    word1: 비교할 첫 번째 단어
    word2: 비교할 두 번째 단어

  Returns:
    word1이 word2보다 사전 순으로 앞선다면 True, 그렇지 않다면 False
  """
  for i in range(min(len(word1), len(word2))):
    if word1[i] < word2[i]:
      return True
    elif word1[i] > word2[i]:
      return False
  return len(word1) < len(word2)

def main():
  """
  문제를 해결하는 함수입니다.
  """
  n = int(input())
  words = set()
  for _ in range(n):
    word = input().strip()
    words.add(word)

  max_len = max(len(word) for word in words)
  sorted_words = counting_sort(list(words), max_len)

  for word in sorted_words:
    print(word)

if __name__ == "__main__":
  main()