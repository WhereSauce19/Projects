import java.util.Stack;

public class test {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<>();

        stack.push("Cat");
        stack.push("Dog");
        stack.push("CatDog");

        stack.pop();

        System.out.println(stack.peek());
    }
}
