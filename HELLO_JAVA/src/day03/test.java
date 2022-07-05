package day03;

public class test {
	public static void main(String[] args) {
		int x =5;
		int y =0;
		int z =0;
		
		y = x++;
		z = --x;
		System.out.println(x+","+y+","+z);
	}
}
