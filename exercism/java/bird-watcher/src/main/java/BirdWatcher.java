
class BirdWatcher {
    private final int[] birdsPerDay;

    public BirdWatcher(int[] birdsPerDay) {
        this.birdsPerDay = birdsPerDay.clone();
    }

    public int[] getLastWeek() {
        //throw new UnsupportedOperationException("Please implement the BirdCount.getLastWeek() method");
        return birdsPerDay;
    }

    public int getToday() {
        //throw new UnsupportedOperationException("Please implement the BirdCount.getToday() method");
        if (birdsPerDay.length == 0){
            return 0;
        }
        return birdsPerDay[birdsPerDay.length -1];
    }

    public void incrementTodaysCount() {
        //throw new UnsupportedOperationException("Please implement the BirdCount.incrementTodaysCount() method");
        birdsPerDay[birdsPerDay.length -1] += 1;
    }

    public boolean hasDayWithoutBirds() {
        //throw new UnsupportedOperationException("Please implement the BirdCount.hasDayWithoutBirds() method");
        boolean dayWithoutBirds = false;
        for (int visits:birdsPerDay){
            if (visits == 0){
                dayWithoutBirds = true;
            }
        }
        return dayWithoutBirds;
    }

    public int getCountForFirstDays(int numberOfDays) {
        //throw new UnsupportedOperationException("Please implement the BirdCount.getCountForFirstDays() method");
        int count = 0;
        for (int i = 0; i < birdsPerDay.length; i++) {
            if (i >= numberOfDays) {
                break;
            } else {
                count += birdsPerDay[i];
            }
        }
        return count;
    }

    public int getBusyDays() {
        //throw new UnsupportedOperationException("Please implement the BirdCount.getBusyDays() method");
        int count = 0;
        for (int i = 0; i < birdsPerDay.length; i++) {
            if (birdsPerDay[i] >= 5) {
                count += 1;
            }
        }
        return count;
    }
}
