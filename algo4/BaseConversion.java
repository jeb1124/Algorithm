package algo4;

import java.util.Scanner;

public class BaseConversion {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s=sc.next();
		int b=sc.nextInt();
		int len=s.length();
		int sum=0;
		int number=0;
		
		for(int i=0; i<len; i++) {
			if(s.charAt(i)>=65) number=s.charAt(i)-55;
			else number=s.charAt(i)-'0';
			int a = (int) Math.pow(b, len-i-1);
			sum += a*number;
		}
		System.out.println(sum);
	}

}
