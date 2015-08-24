class me{
	public static void main(String[] args){
		int []ans=mine(args);
		System.out.println(ans[0] +","+ ans[1]);
		}
	public static int[] mine(String[] args) {
		int a=Integer.parseInt(args[0]);
		int b=Integer.parseInt(args[1]),t;
		int c=a,d=b;
		int[] ans=new int[2];
		if ( a <= 0 || b<=0) { ans[0]=0;ans[1]=0; return ans;}
		while (b!=0) {
			t=b;
			b = a%b;
			a =t;
			}
		boolean first;
		first=	(c>d) ? true:false ;
		if (first==true){
			for (int var=2;;++var){
				if (c-var*d == a){
					ans[0]=1;ans[1]=-var;return ans;
					}
				}
			}
		else{
			if (c==d) { ans[0]=ans[1]=1; return ans;}
			else {
				for ( int var=2;;++var){

					if (var*c-d == a){
						ans[0]=var;ans[1]=-1;
						return ans;
						}
					}
				}
			}
		}
	}
	
