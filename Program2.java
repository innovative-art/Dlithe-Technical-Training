public class Program2 {
    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (i == 0 && j == 4)
                    System.out.print(2);
                else if (i == 1 && j == 0)
                    System.out.print(3);
                else if (i == 2 && j == 4)
                    System.out.print(4);
                else if (i == 3 && j == 0)
                    System.out.print(5);
                else if (i == 4 && j == 4)
                    System.out.print(6);
                else
                    System.out.print(i + 1);
            }
            System.out.println();
        }
    }
}
