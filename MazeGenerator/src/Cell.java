public class Cell {
    int x, y;
    boolean visited = false;
    boolean up = true, down = true, left = true, right = true;

    public Cell(int x, int y) {
        this.x = x;
        this.y = y;
    }
}