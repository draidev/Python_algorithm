
import sys

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
    bucket.sort()
    sorted_words.extend(bucket)

  return sorted_words

def main():
  n = int(sys.stdin.readline())
  words = set()
  for _ in range(n):
    word = sys.stdin.readline().strip()
    words.add(word)

  max_len = max(len(word) for word in words)
  sorted_words = counting_sort(list(words), max_len)

  for word in sorted_words:
    print(word)

if __name__ == "__main__":
  main()