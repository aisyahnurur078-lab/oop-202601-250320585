package id.ac.upb.asetpinjam.model;

public class Ruang extends Aset {

    private int kapasitas;
    private TingkatRisiko tingkatRisiko;

    public Ruang(String kode, String nama, int kapasitas) {
        this(kode, nama, kapasitas, TingkatRisiko.RENDAH);
    }

    public Ruang(String kode, String nama, int kapasitas, TingkatRisiko tingkatRisiko) {
        super(kode, nama);
        if (kapasitas <= 0) {
            throw new IllegalArgumentException("Kapasitas harus lebih dari 0");
        }
        if (tingkatRisiko == null) {
            throw new IllegalArgumentException("Tingkat risiko tidak boleh null");
        }
        this.kapasitas = kapasitas;
        this.tingkatRisiko = tingkatRisiko;
    }

    public int getKapasitas() {
        return kapasitas;
    }

    public TingkatRisiko getTingkatRisiko() {
        return tingkatRisiko;
    }

    @Override
    public JenisAset getJenis() {
        return JenisAset.RUANG;
    }

    @Override
    public long hitungDenda(int hariTerlambat) {
        return hariTerlambat * 5000L;
    }
}