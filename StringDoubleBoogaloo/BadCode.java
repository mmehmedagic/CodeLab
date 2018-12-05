String s = "";  // not counted
String a="";int i,n=0;for(i=0;i<s.length();i++)a+=Long.toString(s.charAt(i),2);for(i=0;i<a.length();i++)n+=Long.valueOf(a.charAt(i)+"");double r=n/2;do r=(r+n/r)/2;while(r*r>n+1e-9);r=1/r;
System.out.println(a + "\n" + n + "\n" + r);  // not counted
