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

    public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
    }

    public int getPrecio() {
		return precio;
	}
	public void setPrecio(int precio) {
		this.precio = precio;
    }

    public Empleado getEmpleadoAsignado() {
		return empleadoAsignado;
	}
	public void setEmpleadoAsignado(Empleado empleadoAsignado) {
		this.empleadoAsignado = empleadoAsignado;
    }
    /*public void consultarDisponibilidad(){

    }*/
}
