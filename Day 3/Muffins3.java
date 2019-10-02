//MUFFINS3

import java.util.*;
import java.lang.*;
import java.io.*;


class Muffins3
{
	public static void main (String[] args)
	{
		Scanner scan = new Scanner(System.in);
		int test_cases = 0;
		if(scan.hasNextInt())
		    test_cases = scan.nextInt();
		while(test_cases -- > 0)
		{
		    int total_cupcakes = scan.nextInt();
		    System.out.println(total_cupcakes / 2 + 1);
		}
	}
}
