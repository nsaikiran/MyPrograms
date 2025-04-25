
public class ParkingLotManager implements ParkingLotNotificationSubscriber {

    Map<VehicleType, ParkingLot> vehicleTypeToLotMap;

    ParkingLotManager(Map<VehicleType, ParkingLot> vehicleTypeToLotMap) {
        this.vehicleTypeToLotMap = vehicleTypeToLotMap;
    }

    public void bookSlotFor(Vehicle v) {

        ParkingLot lot = vehicleToLotMap.get(v.type);

        if (lot.hasFreeSlot()) {
                Price p = lot.getPricePerSlot();
                //Collect paymet of p
                lot.admitVehicle(v);
                return true;
            }
        else {
            //Update board to NO slots
            return false;
        }
        
    }

    @Overrride
    public void parkingLotStatus(VehicleType type, bool isFull) {
        if (isFull) {
            // update parking full board.
        }
        else {
            //update board
        }

    }
}


public enum VehicleType {
    TWO_WHEELER,
    FOUR_WHEELER
    
}