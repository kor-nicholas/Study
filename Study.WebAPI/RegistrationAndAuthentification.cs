// 1. Program/Startup

services.AddDefaultIdentity<IdentityUser>(
  opt => 
  {
    opt.Password.RequireDigit = true; // in pass must use int
    opt.Password.RequireLength = 8;
    opt.Password.RequireUppercase = true; // in pass must use one Upper(big) letter
    opt.Lockout.MaxFailedAccessAttempts = 4; // max try input pass
    opt.User.RequireUniqueEmail = true; // email can't be each in other user
    opt.SignIn.RequireConfirmedEmail = true; email must be confirm
  })
  .AddRoles<IdentityRole>()
  .AddEntityFrameworkStores<[name]DbContext>();
  
app.UseAuthentication();
app.UseAuthorization();

// 2. Ef Core migrations
// dotnet ef migrations add [migration-name]
// dotnet database update

// 3. SeedData (to add default roles/users/...)

// 4. Endpoints and Roles 
[Authorize]
[Authorize(Roles = "Admin/User/...")] (controllers and methods)
