import java.util.*;

class BoundingRobots {

	public static void main(String[] args) {
		BoundingRobots robots = new BoundingRobots();
		Scanner scnr = new Scanner(System.in);
		robots.readInput(scnr);
	}

	public void readInput(Scanner scnr) {
		boolean finished = false;
		while (!finished) {
			int robotX = 0;
			int robotY = 0;
			int actualX = 0;
			int actualY = 0;
			String[] room = scnr.nextLine().trim().split(" ");
			int roomX = Integer.parseInt(room[0]);
			int roomY = Integer.parseInt(room[1]);
			if (roomX == 0 && roomY == 0) return;
			int n = Integer.parseInt(scnr.nextLine());
			for (int i = 0; i < n; i++) {
				String[] move = scnr.nextLine().trim().split(" ");
				System.out.println(Arrays.toString(move));
				String direction = move[0];
				int step = Integer.parseInt(move[1]);
				switch (direction) {
					case "u":
						robotY += step;
						actualX = Math.min(robotY, roomY);
						break;
					case "r":
						robotX += step;
						actualX = Math.min(robotX, roomX);
						break;
					case "d":
						robotY -= step;
						actualX = Math.max(robotY, roomY);
						break;
					case "l":
						robotX -= step;
						actualX = Math.max(robotX, roomX);
						break;
				}
			}
			System.out.printf("Robot thinks %d %d%n", robotX, robotY);
			System.out.printf("Actually at %d %d", actualX, actualY);
			if (scnr.hasNextLine()) System.out.println();
        }
	}
}
