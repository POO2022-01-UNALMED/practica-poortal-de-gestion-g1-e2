package gestorAplicacion;

public class Servicio{
    private String nombre;
    private int precio;
    private Empleado empleadoAsignado;

    public Servicio(String nombre, int precio, Empleado empleadoAsignado){
        this.nombre = nombre;
        this.precio = precio;
        this.empleadoAsignado = empleadoAsignado;
    }

    /*public void consultarDisponibilidad(){

    }*/
}
