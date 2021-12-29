import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[]args) throws Exception{
        try{
            ServerSocket serv = new ServerSocket(1433);
            System.out.println("Server Started");
            Socket soc = serv.accept();
            System.out.println("Client Connected");

            PrintStream ps = new PrintStream(soc.getOutputStream());
            BufferedReader buff = new BufferedReader(new InputStreamReader(soc.getInputStream()));
            BufferedReader kbuff = new BufferedReader(new InputStreamReader(System.in));

            while(true){
                String str1, str2;

                while((str1 = buff.readLine()) != null){
                    System.out.println(str1);
                    str2 = kbuff.readLine();
                    ps.println(str2);
                }

                ps.close();
                buff.close();
                kbuff.close();
                serv.close();
                soc.close();
                
                System.exit(0);
            }
        }
        catch(Exception e){
            System.out.println("Server Error "+e);
        }
    }
}
