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
                currentCell = neighbors.get(random.nextInt(0, (neighbors.size())));
                visitedCells.push(currentCell);
            }
        }

    }
}