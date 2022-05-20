package gestorAplicacion;

public interface Iva {
	public static Double IVA = 0.19;
	
	public abstract int calcularPrecio(int precio);
}
