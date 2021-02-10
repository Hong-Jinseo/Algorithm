import java.util.*;

public class Main_2577 {

	public static void main(String[] args) {
		
		int a, b, c, i=0;
		String result;
		Scanner sc = new Scanner(System.in);
		
		a = sc.nextInt();
		b = sc.nextInt();
		c = sc.nextInt();
		result = Integer.toString(a*b*c);
		
		String[] input = new String[100];
		int[] output = new int[10];
		Arrays.fill(input,"-1");
		
		input = result.split("");
		
		while(Integer.parseInt(input[i])>-1){
			output[Integer.parseInt(input[i])]++;
			i++;
		}
		
		for(int j=0; j<i; j++)
			System.out.println(output[j]);
		
		sc.close();
	}
}
