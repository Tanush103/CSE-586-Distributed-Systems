import java.io.*;
import java.net.*;

class Client {
    public static void main(String[]args) throws Exception{
        try{
            Socket sock = new Socket("server",1433);
            DataOutputStream dos = new DataOutputStream(sock.getOutputStream());
            BufferedReader buff = new BufferedReader(new InputStreamReader(sock.getInputStream()));
            BufferedReader kbuff = new BufferedReader(new InputStreamReader(System.in));

            String str1, str2;

            while(!(str1 = kbuff.readLine()).equals("exit")){
                dos.writeBytes(str1 + "\n");
                str2 = buff.readLine();
                System.out.println(str2);
            }

            dos.close();
            buff.close();
            kbuff.close();
            sock.close();
        }
        catch(Exception e){
            System.out.println("Client Error "+e);
        }
    }
}