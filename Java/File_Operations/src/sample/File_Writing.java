package sample;
import java.io.*;

public class File_Writing {
    public static void main(String[] args) throws Exception{
        String data = "Istiaq Ahmed Fahad";
        char[] chardata = data.toCharArray();
        int mark = 1;
        FileWriter fw = new FileWriter("Output_demo.txt");
        BufferedWriter br = new BufferedWriter(fw);


        for(int i=0; i<data.length(); i++){
            if(i%2==0) {
                br.write(chardata[i]);
                System.out.println(chardata[i]);
            }
        }
        br.close();
    }
}
