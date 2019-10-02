//STRPALIN

import java.util.*;
import java.lang.*;
import java.io.*;


class Strpalin
{
	public static void main (String[] args)
	{
		Scanner scan = new Scanner(System.in);
		int test_cases = 0;
		if(scan.hasNextInt())
		    test_cases = scan.nextInt();
		while(test_cases -- > 0)
		{   
        int found = 0;
		    String s1 = scan.next();
		    String s2 = scan.next();
		    for(int i = 0;i < s1.length();i++)
		    {
		        if(s2.indexOf(s1.charAt(i)) != -1)
	            {
		            found = 1;
		            break;
		          }    
		    }
		    if(found == 1)
		        System.out.println("Yes");
		    else
		        System.out.println("No");
		}
	}
}
