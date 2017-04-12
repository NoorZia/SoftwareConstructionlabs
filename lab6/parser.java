/**
 * Created by noor on 3/29/17.
 */

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class parser {
    public void readCsv() {
        String fileName = "/home/noor/IdeaProjects/lab5/GeoLiteCity-Location.csv";
        File file = new File(fileName);
        int i=0;
        try {
            Scanner inputStream = new Scanner(file);
            while(inputStream.hasNext()){
                if(i<9){
                    String data = inputStream.next();
                    i+=1;
                    continue;
                }
                i+=1;
                String data = inputStream.next();
                System.out.println(data);
                String[] c = data.split(",");
                if(c.length>6){

                    City ok = new City();
                    System.out.println(c[0]);
                    System.out.println(c[3]);
                    System.out.println(Float.parseFloat(c[c.length-1]));
                    System.out.println(Float.parseFloat(c[c.length-2]));
                    ok.setId(Integer.parseInt(c[0]));
                    ok.setCity(c[3]);
                    ok.setLatitude(Float.parseFloat(c[c.length-1]));
                    ok.setLongitude(Float.parseFloat(c[c.length-2]));
                }



            }
            inputStream.close();
        }
        catch (FileNotFoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
        System.out.println("Done with reading CSV");
    }
}