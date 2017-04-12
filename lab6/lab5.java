import com.opencsv.CSVReader;
import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.boot.registry.StandardServiceRegistryBuilder;
import org.hibernate.cfg.Configuration;
import org.hibernate.service.ServiceRegistry;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Created by noor on 3/29/17.
 */
public class lab5 {

    public ArrayList<String> lines = new ArrayList<>();
    public String fileName = "/home/noor/IdeaProjects/lab5/GeoLiteCity-Location1.csv";


    public void readFile() throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(fileName));
        String newLine;
        while ((newLine = br.readLine()) != null) {
            System.out.println(newLine);
            lines.add(newLine);
        }
        br.close();
    }
    public static float [] get_lat_lon(City c){
        float [] latlon= new float[2];
        latlon[0]=c.getLatitude();
        latlon[1]=c.getLongitude();
        return latlon;
    }


    public static void main(String[] args) {

      Configuration cfg=new Configuration();
        cfg.configure("config.cfg.xml");//populates the data of the configuration file
       // cfg.addClass(City.class);
        //creating seession factory object
        ServiceRegistry serviceRegistry = new StandardServiceRegistryBuilder().applySettings(cfg.getProperties()). build();
        SessionFactory factory=cfg.buildSessionFactory(serviceRegistry);
        //creating session object
      Session session=factory.openSession();

    lab5 lab5Handler = new lab5();
        try {
            lab5Handler.readFile();
            for(int i=0;i<3000;i++){
                System.out.println(lab5Handler.lines.get(i));
                if(i>0) {
                    String line = lab5Handler.lines.get(i);
                    System.out.println(line);
                    String[] c = line.split(",");
                   /*Transaction t = session.beginTransaction();
                    City ok = new City();
                    // ['locId', 'country', 'region', 'city', 'postalCode', 'latitude', 'longitude', 'metroCode', 'areaCode']
                    ok.setId(Integer.parseInt(c[0]));
                    ok.setCountry(c[1]);
                    ok.setRegion(c[2]);
                    ok.setCity(c[3]);
                    ok.setPostalcode(Integer.parseInt(c[4]));
                    ok.setLatitude(Float.parseFloat(c[5]));
                    ok.setLongitude(Float.parseFloat(c[5]));
                    ok.setMetrocode(Integer.parseInt(c[7]));
                    ok.setAreacode(Integer.parseInt(c[8]));
                    session.persist(ok);//persisting the object
                    t.commit();//transaction is commited*/
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Enter 1st name");
        Scanner SC=new Scanner(System.in);
        String first=SC.nextLine();
        session=factory.openSession();

        System.out.println("Enter 2nd name");
        Scanner Sc=new Scanner(System.in);
        String second=Sc.nextLine();

        String hql = "FROM City  WHERE city like '%"+first+"%'";
        String hql1 = "FROM City  WHERE city like '%"+second+"%'";
        Query query = session.createQuery(hql);
        Query query1 = session.createQuery(hql1);
        //queryy.setParameter("city", "Atlanta");
        List<City> result = query.list();
        List<City> result1 = query1.list();

       City c1=(City)result.get(0);
        City c2=(City)result1.get(0);
        System.out.print(c1.getCity());
        GreatCircle gc = new GreatCircle();
        float [] latlon1 =get_lat_lon(c1),latlon2=get_lat_lon(c2);
       double distance =  gc.getDistance(latlon1[0],latlon1[1], latlon2[0], latlon2[1]);

        System.out.println("Distance between both cities = "+ distance);
        System.out.println("City 1 latitude and longitude = "+ latlon1[0]+ " "+ latlon1[1]);
        System.out.println("City 2 latitude and longitude = "+ latlon2[0]+ " "+ latlon2[1]);

        System.out.println("Enter Name of City to Search (n) nearest Cities");
        Scanner SC1=new Scanner(System.in);
        String name=SC1.nextLine();
        System.out.println("Enter number of closest cities");
        int choice= SC1.nextInt();


        String hql2 = "FROM City where city like '%"+name+"%'";
        Query query2 = session.createQuery(hql2);
        List result2= query2.list();
        City C= (City)result2.get(0);
        float []latlon= get_lat_lon(C);



        hql2 = "FROM  City c where length(city)>2  and sqrt((power(lat,2)-power("+latlon[0]+",2))+(power(lon,2)-power("+latlon[1]+",2))) is not null   order by sqrt((power(lat,2)-power("+latlon[0]+",2))+(power(lon,2)-power("+latlon[1]+",2))) ";


        query2 = session.createQuery(hql2);
        query2.setFirstResult(0);
        query2.setMaxResults(choice+1);

        //queryy.setParameter("city", "Atlanta");
        result = query.list();

        for (City c3 : result){

            System.out.println("Distance is: "+gc.getDistance(c3.getLatitude(),c3.getLongitude(), latlon[0], latlon[1]));
            System.out.println("City name is: "+c3.getCity());
            System.out.println();

        }

        session.close();

      //////////////////////////




    }

}
