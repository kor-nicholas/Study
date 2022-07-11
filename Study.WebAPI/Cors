// in Program/Startup

services.AddCors();

app.UseCors(options => 
  options.WithOrigins("https://[domain-name]", "http:localhost:2000")
  .AllowAnyMethod()
  .AllowAnyHeader()
  .AllowCredentials());
  
