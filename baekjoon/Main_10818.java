import java.util.*;

public class Main_10818 {

	public static void main(String[] args) {
		int max, min, cnt, num;
		
		Scanner sc = new Scanner(System.in);
		cnt = sc.nextInt();
		max = min = sc.nextInt();
		
		for(int i=0; i<cnt-1; i++) {
			num = sc.nextInt();
			if(num>max) max=num;
			if(num<min) min=num;
		}

		System.out.print(min+" "+max);
		sc.close();
	}
}
