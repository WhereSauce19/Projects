import java.util.ArrayList;
import java.util.Random;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Random random = new Random();
        Stack<Cell> visitedCells = new Stack<>();
        int rows = 5, columns = 5;

        Cell[][] grid = new Cell[rows][columns];

        for (int x = 0; x < columns; x++) {
            for (int y = 0; y < rows; y++) {
                grid[x][y] = new Cell(x, y);
            }
        }

        Cell currentCell = grid[0][0];
        currentCell.left = false;

        currentCell.visited = true;
        visitedCells.push(currentCell);
        int visitedCount = 1;

        while (visitedCount < (rows * columns)) {
            ArrayList<Cell> neighbors = new ArrayList<>();

            if (currentCell.y > 0) {
                Cell neighborUp = grid[currentCell.x][currentCell.y - 1];
                if (neighborUp.visited == false) {
                    neighbors.add(neighborUp);
                }
            }
            if (currentCell.y < (rows - 1)) {
                Cell neighborDown = grid[currentCell.x][currentCell.y + 1];
                if (neighborDown.visited == false) {
                    neighbors.add(neighborDown);
                }
            }
            if (currentCell.x > 0) {
                Cell neighborLeft = grid[currentCell.x - 1][currentCell.y];
                if (neighborLeft.visited == false) {
                    neighbors.add(neighborLeft);
                }
            }
            if (currentCell.x < (columns - 1)) {
                Cell neighborRight = grid[currentCell.x + 1][currentCell.y];
                if (neighborRight.visited == false) {
                    neighbors.add(neighborRight);
                }
            }

            if (!currentCell.visited) {
                visitedCount += 1;
            }
            currentCell.visited = true;

            if (neighbors.isEmpty()) {
                visitedCells.pop();
                currentCell = visitedCells.peek();
            } else {
                Cell nextCell = neighbors.get(random.nextInt(0, (neighbors.size())));
                int nextCellDirection;
                if (currentCell.x != nextCell.x) {
                    nextCellDirection = nextCell.x - currentCell.x;
                    if (nextCellDirection == -1) {
                        currentCell.left = false;
                    } else if (nextCellDirection == 1) {
                        currentCell.right = false;
                    }
                    if (currentCell.x != columns - 1) {
                        currentCell.left = grid[currentCell.x + 1][currentCell.y].right;
                    }

                } else if (currentCell.y != nextCell.y) {
                    nextCellDirection = nextCell.y - currentCell.y;
                    if (nextCellDirection == 1) {
                        currentCell.down = false;
                    } else if (nextCellDirection == -1) {
                        currentCell.up = false;
                    }
                    if (currentCell.y != rows - 1) {
                        currentCell.down = grid[currentCell.x][currentCell.y + 1].up;
                    }
                }

                currentCell = nextCell;
                visitedCells.push(currentCell);

            }
        }

        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < columns; x++) {
                System.out.print("+");
                if (grid[x][y].up) {
                    System.out.print("---");
                } else {
                    System.out.print("   ");
                }
            }
            System.out.print("+\n");

            for (int x = 0; x < columns; x++) {

                if (grid[x][y].left) {
                    System.out.print("|   ");
                } else {
                    System.out.print("   ");
                }
            }
            System.out.print("\n");

        }

    }
}