def min_length(N, Value, Point):
  # Initialize window pointers and answer
  i, j, ans = 0, 0, 0

  # Loop through the array
  while j < N:
    # Calculate maximum distance and total distance within the window
    max_dist, total_distance = 0, 0
    for k in range(i, j + 1):
      if k + 1 < N:
        total_distance += Point[k + 1] - Point[k]
        max_dist = max(max_dist, Point[k + 1] - Point[k])

    # Update answer based on window location
    if i == 0 or j == N - 1:
      ans += total_distance
    else:
      ans += total_distance - max_dist

    # Move to the next group of points
    while j + 1 < N and Value[j] == Value[j + 1]:
      j += 1
    i = j + 1

  # Print the answer
  print(ans)

# Driver function
if __name__ == "__main__":
  N = 8
  Value = [1, 0, 1, 0, 0, 1, 1, 0]
  Point = [1, 5, 6, 7, 11, 14, 16, 18]

  min_length(N, Value, Point)
