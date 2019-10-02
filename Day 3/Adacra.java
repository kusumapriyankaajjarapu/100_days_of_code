//ADACRA

import java.util.*;
import java.lang.*;
import java.io.*;


class Adacra
{
	public static void main (String[] args) 
	{
	    Scanner scan = new Scanner(System.in);
		  int test_cases = 0;
		  if(scan.hasNextInt())
		    test_cases = scan.nextInt();
		  while(test_cases -- > 0)
		  {
		      String crayons = scan.next();
		      char ch = crayons.charAt(0);
		      int u_count = 0,d_count = 0;
		      if(ch == 'U')
		        u_count++;
		      else
		        d_count++;
		      for(int i = 1;i < crayons.length();i++)
		      {
		        if(ch != crayons.charAt(i))
		        {
		            ch = crayons.charAt(i);
		            if(ch == 'U')
		                u_count++;
		            else
		                d_count++;
		        }
		        
		      }
		      if(u_count > d_count)
		        System.out.println(d_count);
		      else
		        System.out.println(u_count);
		  }
	  }
} 
