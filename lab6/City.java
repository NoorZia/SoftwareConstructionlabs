import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;


public class City {

    private int id;
    private int postalcode;
    private String region,city,country;
    private float latitude,longitude;
    private int metrocode, areacode;

    public int getId() {
        return id;
    }

    public void setPostalcode(int postalcode) {
        this.postalcode = postalcode;
    }

    public int getPostalcode() {
        return postalcode;
    }

    public int getAreacode() {
        return areacode;
    }

    public float getLatitude() {
        return latitude;
    }

    public float getLongitude() {
        return longitude;
    }

    public int getMetrocode() {
        return metrocode;
    }

    public String getCity() {
        return city;
    }


    public String getCountry() {
        return country;
    }

    public String getRegion() {
        return region;
    }

    public void setAreacode(int areacode) {
        this.areacode = areacode;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setLatitude(float latitude) {
        this.latitude = latitude;
    }

    public void setLongitude(float longitude) {
        this.longitude = longitude;
    }

    public void setMetrocode(int metrocode) {
        this.metrocode = metrocode;
    }

    public void setRegion(String region) {
        this.region = region;
    }

    public String toString(){
        return "City{ id="+this.id+", city="+this.city+",lat="+this.latitude+", lon="+this.longitude+"}";
    }
}
