package gestorAplicacion;
import java.time.LocalDate; // import the LocalDate class

public class Documento {
    String nombre;
    LocalDate fechaExpedicion;
    Empleado expedidoPor;
    public Documento(String nombre, LocalDate fechaExpedicion, Empleado expedidoPor) {
        this.nombre = nombre;
        this.fechaExpedicion = fechaExpedicion;
        this.expedidoPor = expedidoPor;
    }
}
