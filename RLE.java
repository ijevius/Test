import java.util.Scanner;
import java.util.regex.*;

class RLE {

    static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		String src = sc.nextLine();
        System.out.println(l(src));
    }

	static int l(String e){
		int total = 0;
		char[] o = e.toCharArray();
		String right; String p = "\\d+";
		Pattern pattern = Pattern.compile(p);
		Matcher matcher;
		for(int i=0; i<o.length; i++){
			if(l(o[i])){
				if(i==o.length-1){
					total++;
			    }else{
		            if(!l(o[i+1])){
				        right = e.substring(i+1, e.length());
				        matcher = pattern.matcher(right);
				        if(matcher.find()){
				            total += Integer.parseInt(matcher.group());
					    }else{
						    total++;
				        }
			        }else{
				        total++;
			        }
		        }
		    }
		}
		
		return total;
	}

	static boolean l(char c){
		return Character.isLetter(c);
	}
	
}
