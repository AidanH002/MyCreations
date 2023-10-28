import java.math.BigInteger;
import java.util.Scanner;

public class FibonacciCalculator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the position of Fibonacci number to calculate: ");
        int n = scanner.nextInt(); // Fibonacci number position input from user
        scanner.close();

        BigInteger fibN = calculateFibonacci(n);
        System.out.println("The " + n + "th Fibonacci number is: " + fibN);
    }

    public static BigInteger calculateFibonacci(int n) {
        BigInteger[][] matrix = {{BigInteger.ONE, BigInteger.ONE}, {BigInteger.ONE, BigInteger.ZERO}};
        BigInteger[][] result = matrixPower(matrix, n - 1);
        return result[0][0];
    }

    public static BigInteger[][] matrixMultiply(BigInteger[][] a, BigInteger[][] b) {
        BigInteger[][] c = new BigInteger[2][2];
        c[0][0] = a[0][0].multiply(b[0][0]).add(a[0][1].multiply(b[1][0]));
        c[0][1] = a[0][0].multiply(b[0][1]).add(a[0][1].multiply(b[1][1]));
        c[1][0] = a[1][0].multiply(b[0][0]).add(a[1][1].multiply(b[1][0]));
        c[1][1] = a[1][0].multiply(b[0][1]).add(a[1][1].multiply(b[1][1]));
        return c;
    }

    public static BigInteger[][] matrixPower(BigInteger[][] matrix, int n) {
        if (n == 0) {
            return new BigInteger[][] {{BigInteger.ONE, BigInteger.ZERO}, {BigInteger.ZERO, BigInteger.ONE}};
        } else if (n % 2 == 0) {
            BigInteger[][] temp = matrixPower(matrix, n / 2);
            return matrixMultiply(temp, temp);
        } else {
            return matrixMultiply(matrix, matrixPower(matrix, n - 1));
        }
    }
}
