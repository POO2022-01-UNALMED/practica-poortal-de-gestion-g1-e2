package gestorAplicacion;
import java.util.ArrayList;
import java.time.LocalDate; // import the LocalDate class

public class Factura {
    private int consecutivo;
    private int total;
    private int cambio;
    private ArrayList<Producto> productos;
    private ArrayList<Servicio> servicios;

    public Factura(int consecutivo, int total, int cambio, Producto producto, Servicio servicio) {
        this.consecutivo = consecutivo;
        this.productos.add(producto);
        this.servicios.add(servicio);
    }

    // public ArrayList<Factura> buscarFacturasPorFecha(LocalDate fechaInicio, LocalDate fechaFin) {

    // }

    // public int calcularCostoTotal(){

    // }
}
