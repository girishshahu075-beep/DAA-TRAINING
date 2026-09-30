class Solution {
    public int racecar(int target) {
           Queue<int[]> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.add(new int[]{0, 1, 0});
        visited.add("0,1");

        while (!queue.isEmpty()) {

            int[] current = queue.poll();

            int position = current[0];
            int speed = current[1];
            int steps = current[2];

            if (position == target) {
                return steps;
            }

            // A
            int newPosition = position + speed;
            int newSpeed = speed * 2;

            if (Math.abs(newPosition) <= 2 * target) {

                String state = newPosition + "," + newSpeed;

                if (!visited.contains(state)) {
                    visited.add(state);
                    queue.add(new int[]{newPosition, newSpeed, steps + 1});
                }
            }

            // R
            if (speed > 0) {
                newSpeed = -1;
            } else {
                newSpeed = 1;
            }

            String state = position + "," + newSpeed;

            if (!visited.contains(state)) {
                visited.add(state);
                queue.add(new int[]{position, newSpeed, steps + 1});
            }
        }

        return -1;
    }
}
