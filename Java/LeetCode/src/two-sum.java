//https://leetcode.com/problems/two-sum/
//Reprak11

import java.util.Arrays;
import java.util.Scanner;

class twoSum {
public static void main (String[] args){
    Scanner scan = new Scanner(System.in);

    String arrayofnumber  = scan.next();
    arrayofnumber=arrayofnumber.substring(1,arrayofnumber.length()-1);
    String [] values= arrayofnumber.split(",");
    int [] nums = new int [values.length];
    for (int i=0;i<values.length;i++){
        nums[i]=Integer.parseInt(values[i]);
    }

    int target = scan.nextInt();

    int [] resultados = twoSum(nums,target);

    System.out.println(Arrays.toString(resultados));

}


public static int[] twoSum(int[] nums, int target) {
    int [] datos= new int [2];
    for (int i=0; i < nums.length-1; i++)
    {
        for (int j = i + 1; j < nums.length;j++)
        {
            if ((nums[i]+nums[j])==target){
                datos[0]=i;
                datos[1]=j;
                return datos;
            }
        }
    }
    
    return datos; 
}
}