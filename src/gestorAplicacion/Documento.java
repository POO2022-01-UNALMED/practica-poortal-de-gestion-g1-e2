package gestorAplicacion;
import java.time.LocalDate; // import the LocalDate class

public abstract class Documento {
    String nombre;
    LocalDate fechaExpedicion;

    public Documento(String nombre, LocalDate fechaExpedicion, Empleado expedidoPor) {
        this.nombre = nombre;
        this.fechaExpedicion = fechaExpedicion;
    }
    
    public abstract String generarIdentificador();
}
