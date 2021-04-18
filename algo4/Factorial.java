package algo4;

import java.util.Scanner;

public class Factorial {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int result = factorial(n);
		System.out.println(result);
	}
	
	public static int factorial(int number) {
		if(number<2)
			return 1;
		else
			return number * factorial(number-1);
	}
}
