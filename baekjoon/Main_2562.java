import java.util.*;

public class Main_2562 {

	public static void main(String[] args) {
		
		int max=0, index=0, num;
		
		Scanner sc = new Scanner(System.in);			;
		for(int i=1; i<=9; i++) {
			num = sc.nextInt();
			if(num>max) {
				max=num;
				index = i;
			}
		}
		
		System.out.println(max);
		System.out.println(index);
		
		sc.close();		
	}
}
