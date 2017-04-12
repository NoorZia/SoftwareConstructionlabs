public class GreatCircle {
    public double getDistance(float x1, float y1, float x2, float y2) {
//        float x1 = Math.toRadians(Double.parseDouble(args[0]));
//        double y1 = Math.toRadians(Double.parseDouble(args[1]));
//        double x2 = Math.toRadians(Double.parseDouble(args[2]));
//        double y2 = Math.toRadians(Double.parseDouble(args[3]));

       /*************************************************************************
         * Compute using law of cosines
         *************************************************************************/
       double xx1 = Double.parseDouble(Float.toString(x1));
        double xx2 = Double.parseDouble(Float.toString(x2));
        double yy1 = Double.parseDouble(Float.toString(y1));
        double yy2 = Double.parseDouble(Float.toString(y2));
        // great circle distance in radians
       double angle1 = Math.acos(Math.sin(xx1) *Math.sin(xx2)
                + Math.cos(xx1) * (double) Math.cos(xx2) * (double) Math.cos(yy1 - yy2));

       // convert back to degrees
        angle1 = (float)Math.toDegrees(angle1);

       // each degree on a great circle of Earth is 60 nautical miles
       double distance1 = 60 * angle1;
        return distance1;
        //System.out.println(distance1 + " nautical miles");

   }
}
