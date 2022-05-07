package gestorAplicacion;
import java.time.LocalDate; // import the LocalDate class

public class Contrato {
    private int salario;
    LocalDate fechaInicio;
    LocalDate fechaFin;

    public Contrato(int salario, LocalDate fechaInicio, LocalDate fechaFin) {
        this.salario = salario;
        this.fechaInicio = fechaInicio;
        this.fechaFin = fechaFin;
    }
    public boolean consultarVigencia(Contrato contrato){
        LocalDate hoy = LocalDate.now();
        return hoy.isAfter(fechaFin);
    }
}