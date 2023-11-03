import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Santa here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Santa extends Actor
{
    private int gunReloadTime;              // The minimum delay between firing the gun.
    private int reloadDelayCount;           // How long ago we fired the gun the last time.
    private int acceleration;            // A vector used to accelerate when using booster.
    private int shotsFired;                 // Number of shots fired.
    int speed = 5;
    public Santa()
    {
        gunReloadTime = 50;
        reloadDelayCount = 0;
        shotsFired = 0;
    }
    public void act() 
    {
        checkKeyPress();
        reloadDelayCount++;
        checkCollision();
    }
        private void checkKeyPress()
    {
        if (Greenfoot.isKeyDown("w")) 
        {
            setLocation(getX(), getY()-3);
        }
        if (Greenfoot.isKeyDown("s")) 
        {
            setLocation(getX(), getY()+3);
        }
        if (Greenfoot.isKeyDown("a")) 
        {
            setLocation(getX()-3, getY());
        }
        if (Greenfoot.isKeyDown("d")) 
        {
            setLocation(getX()+3, getY());
        }
        if (Greenfoot.isKeyDown("space")) 
        {
            fire();
        }
    }
    public int getShotsFired()
    {
        return shotsFired;
    }
    /**
     * Set the time needed for re-loading the rocket's gun. The shorter this time is,
     * the faster the rocket can fire. The (initial) standard time is 20.
     */
    public void setGunReloadTime(int reloadTime)
    {
        gunReloadTime = reloadTime;
    }
    public void fire() 
    {
        if (reloadDelayCount >= gunReloadTime)
        {
            Snowball b = new Snowball(speed);
            getWorld().addObject(b, getX(), getY());
            b.move(speed);
            shotsFired++;
            reloadDelayCount = 0;   // time since last shot fired
        }
    } 
    private void checkCollision()
    {
        if (isTouching(Present.class))
        {
            removeTouching(Present.class);
            MyWorld myWorld = (MyWorld)getWorld();
            myWorld.addScore(10);
        }
        if (isTouching(Robot.class))
        {
            removeTouching(Robot.class);
            MyWorld myWorld = (MyWorld)getWorld();
            myWorld.addScore(-50);
        }
        if (isTouching(Bullet.class))
        {
            removeTouching(Bullet.class);
            MyWorld myWorld = (MyWorld)getWorld();
            myWorld.addScore(-5);
        }
    }
}
