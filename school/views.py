from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import connection
import json
import re

# Create your views here.
class CarreerView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, key=None):
        cursor = connection.cursor()
        if key != None:
            cursor.execute("SELECT * FROM carrera WHERE clave = %s", [key])
            carreers = cursor.fetchall()
            json_data = []
            try:
                json_data.append({'clave': carreers[0][0], 'nombre': carreers[0][1], 'fecalt': carreers[0][2], 'fecbaj': carreers[0][3]})
            except Exception as e:
                data = {
                    'message': 'No se encontró la carrera con clave: ' + str(key),
                    'error': re.split(r'\n', str(e))
                }
            else:
                data = {
                    'message': 'Carrera encontrada',
                    'carreer': json_data
                }
            finally:
                cursor.close()
            return JsonResponse(data)
        else:
            cursor.execute("SELECT * FROM carrera")
            carreers = cursor.fetchall()
            json_data = []
            try:
                for carreer in carreers:
                    json_data.append({'clave': carreer[0], 'nombre': carreer[1], 'fecalt': carreer[2], 'fecbaj': carreer[3]})
            except Exception as e:
                data = {
                    'message': 'No se encontraron carreras',
                    'error': re.split(r'\n', str(e))
                }
            else:
                data = {
                    'message': 'Carreras encontradas',
                    'carreers': json_data
                }
            finally:
                cursor.close()
            return JsonResponse(data)
    
    def post(self, request):
        cursor = connection.cursor()
        jd = json.loads(request.body)
        try:
            cursor.execute("INSERT INTO carrera VALUES (%s, %s, %s, %s)", [jd['clave'], jd['nombre'], jd['fecalt'], jd['fecbaj']])
        except Exception as e:
            data = {
                'message': 'No se pudo insertar la carrera',
                'error': re.split(r'\n', str(e))
            }
        else:
            data = {
                'message': 'Carrera insertada'
            }
        finally:
            cursor.close()
        return JsonResponse(data)
    
    def put(self, request, key=None):
        cursor = connection.cursor()
        jd = json.loads(request.body)
        try:
            cursor.execute("UPDATE carrera SET nombre = %s, fecalt = %s, fecbaj = %s WHERE clave = %s", [jd['nombre'], jd['fecalt'], jd['fecbaj'], key])
        except Exception as e:
            data = {
                'message': 'No se pudo actualizar la carrera',
                'error': re.split(r'\n', str(e))
            }
        else:
            data = {
                'message': 'Carrera actualizada'
            }
        finally:
            cursor.close()
        return JsonResponse(data)
    
    def delete(self, request, key=None):
        cursor = connection.cursor()
        carreer = [key]
        try:
            cursor.execute("DELETE FROM carrera WHERE clave = %s", carreer)
        except Exception as e:
            data = {
                'message': 'No se pudo eliminar la carrera',
                'error': re.split(r'\n', str(e))
            }
        else:
            data = {
                'message': 'Carrera eliminada'
            }
        finally:
            cursor.close()
        return JsonResponse(data)
    
class SubjectView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, key=None):
        cursor = connection.cursor()
        if key != None:
            cursor.execute("SELECT * FROM materia WHERE clave = %s", [key])
            subjects = cursor.fetchall()
            json_data = []
            try:
                json_data.append({'clave': subjects[0][0], 'descri': subjects[0][1], 'nsesio': subjects[0][2], 'durses': subjects[0][3], 'taller': subjects[0][4], 'fecalt': subjects[0][5], 'fecbaj': subjects[0][6], 'tipo': subjects[0][7]})
            except Exception as e:  
                data = {
                    'message': 'No se encontró la materia con clave: ' + str(key),
                    'error': re.split(r'\n', str(e))
                }
            else:
                data = {
                    'message': 'Materia encontrada',
                    'subject': json_data
                }
            finally:
                cursor.close()
            return JsonResponse(data)
        else:
            cursor.execute("SELECT * FROM materia")
            subjects = cursor.fetchall()
            json_data = []
            try:
                for subject in subjects:
                    json_data.append({'clave': subject[0], 'descri': subject[1], 'nsesio': subject[2], 'durses': subject[3], 'taller': subject[4], 'fecalt': subject[5], 'fecbaj': subject[6], 'tipo': subject[7]})
            except Exception as e:
                data = {
                    'message': 'No se encontraron materias',
                    'error': re.split(r'\n', str(e))
                }
            else:
                data = {
                    'message': 'Materias encontradas',
                    'subjects': json_data
                }
            finally:
                cursor.close()
            return JsonResponse(data)
        
    def post(self, request):
        cursor = connection.cursor()
        jd = json.loads(request.body)
        try:
            cursor.execute("INSERT INTO materia VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", [jd['clave'], jd['descri'], jd['nsesio'], jd['durses'], jd['taller'], jd['fecalt'], jd['fecbaj'], jd['tipo']])
        except Exception as e:
            data = {
                'message': 'No se pudo insertar la materia',
                'error': re.split(r'\n', str(e))
            }
        else:
            data = {
                'message': 'Materia insertada'
            }
        finally:
            cursor.close()
        return JsonResponse(data)
    
    def put(self, request, key=None):
        cursor = connection.cursor()
        jd = json.loads(request.body)
        try:
            cursor.execute("UPDATE materia SET descri = %s, nsesio = %s, durses = %s, taller = %s, fecalt = %s, fecbaj = %s, tipo = %s WHERE clave = %s", [jd['descri'], jd['nsesio'], jd['durses'], jd['taller'], jd['fecalt'], jd['fecbaj'], jd['tipo'], key])
        except Exception as e:
            data = {
                'message': 'No se pudo actualizar la materia',
                'error': re.split(r'\n', str(e))
            }
        else:
            data = {
                'message': 'Materia actualizada'
            }
        finally:
            cursor.close()
        return JsonResponse(data)
    
    def delete(self, request, key=None):
        cursor = connection.cursor()
        subject = [key]
        try:
            cursor.execute("DELETE FROM materia WHERE clave = %s", subject)
        except Exception as e:
            data = {
                'message': 'No se pudo eliminar la materia',
                'error': re.split(r'\n', str(e))
            }
        else:
            data = {
                'message': 'Materia eliminada'
            }
        finally:
            cursor.close()
        return JsonResponse(data)
    
class PlanView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, key1=None, key2=None):
        cursor = connection.cursor()
        if key1 != None and key2 != None:
            cursor.execute("SELECT clave, carreer_id, materi_id, fecalt, fecbaj, area, reqsim, requi1, requi2, requi3, requi4, semest FROM plan WHERE carreer_id = %s AND materi_id = %s", [key1, key2])
            plans = cursor.fetchall()
            json_data = []
            try:
                json_data.append({'clave': plans[0][0], 'carrer': plans[0][1], 'materi': plans[0][2], 'fecalt': plans[0][3], 'fecbaj': plans[0][4], 'area': plans[0][5], 'reqsim': plans[0][6], 'requi1': plans[0][7], 'requi2': plans[0][8], 'requi3': plans[0][9], 'requi4': plans[0][10], 'semest': plans[0][11]})
            except Exception as e:
                data = {
                    'message': 'No se encontró el plan con clave: ' + str(key),
                    'error': re.split(r'\n', str(e))
                }
            else:
                data = {
                    'message': 'Plan encontrado',
                    'plan': json_data
                }
            finally:
                cursor.close()
            return JsonResponse(data)
        else:
            cursor.execute("SELECT clave, carreer_id, materi_id, fecalt, fecbaj, area, reqsim, requi1, requi2, requi3, requi4, semest FROM plan")
            plans = cursor.fetchall()
            json_data = []
            try:
                for plan in plans:
                    json_data.append({'clave': plan[0], 'carrer': plan[1], 'materi': plan[2], 'fecalt': plan[3], 'fecbaj': plan[4], 'area': plan[5], 'reqsim': plan[6], 'requi1': plan[7], 'requi2': plan[8], 'requi3': plan[9], 'requi4': plan[10], 'semest': plan[11]})
            except Exception as e:
                data = {
                    'message': 'No se encontraron planes',
                    'error': re.split(r'\n', str(e))
                }
            else:
                data = {
                    'message': 'Planes encontrados',
                    'plans': json_data
                }
            finally:
                cursor.close()
            return JsonResponse(data)
    
    def post(self, request):
        cursor = connection.cursor()
        jd = json.loads(request.body)
        try:
            cursor.execute("INSERT INTO plan (clave, fecalt, fecbaj, area, reqsim, requi1, requi2, requi3, requi4, semest, carreer_id, materi_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [jd['clave'], jd['fecalt'], jd['fecbaj'], jd['area'], jd['reqsim'], jd['requi1'], jd['requi2'], jd['requi3'], jd['requi4'], jd['semest'], jd['carrer'], jd['materi']])
        except Exception as e:
            data = {
                'message': 'No se pudo insertar el plan',
                'error': re.split(r'\n', str(e))
            }
        else:
            data = {
                'message': 'Plan insertado'
            }
        finally:
            cursor.close()
        return JsonResponse(data)
    
    def put(self, request, key1=None, key2=None):
        cursor = connection.cursor()
        jd = json.loads(request.body)
        print(jd)
        try:
            cursor.execute("UPDATE plan SET fecalt = %s, fecbaj = %s, area = %s, reqsim = %s, requi1 = %s, requi2 = %s, requi3 = %s, requi4 = %s, semest = %s WHERE carreer_id = %s AND materi_id = %s", [jd['fecalt'], jd['fecbaj'], jd['area'], jd['reqsim'], jd['requi1'], jd['requi2'], jd['requi3'], jd['requi4'], jd['semest'], key1, key2])
        except Exception as e:
            data = {
                'message': 'No se pudo actualizar el plan',
                'error': re.split(r'\n', str(e))
            }
        else:
            data = {
                'message': 'Plan actualizado'
            }
        finally:
            cursor.close()
        return JsonResponse(data)
    
    def delete(self, request, key1=None, key2=None):
        cursor = connection.cursor()
        plan = [key1, key2]
        try:
            cursor.execute("DELETE FROM plan WHERE carreer_id = %s AND materi_id = %s", plan)
        except Exception as e:
            data = {
                'message': 'No se pudo eliminar el plan',
                'error': re.split(r'\n', str(e))
            }
        else:
            data = {
                'message': 'Plan eliminado'
            }
        finally:
            cursor.close()
        return JsonResponse(data)
                