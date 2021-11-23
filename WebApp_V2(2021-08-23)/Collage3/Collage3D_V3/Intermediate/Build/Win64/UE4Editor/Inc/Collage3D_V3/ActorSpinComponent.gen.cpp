// Copyright Epic Games, Inc. All Rights Reserved.
/*===========================================================================
	Generated code exported from UnrealHeaderTool.
	DO NOT modify this manually! Edit the corresponding .h files instead!
===========================================================================*/

#include "UObject/GeneratedCppIncludes.h"
#include "Collage3D_V3/ActorSpinComponent.h"
#ifdef _MSC_VER
#pragma warning (push)
#pragma warning (disable : 4883)
#endif
PRAGMA_DISABLE_DEPRECATION_WARNINGS
void EmptyLinkFunctionForGeneratedCodeActorSpinComponent() {}
// Cross Module References
	COLLAGE3D_V3_API UClass* Z_Construct_UClass_UActorSpinComponent_NoRegister();
	COLLAGE3D_V3_API UClass* Z_Construct_UClass_UActorSpinComponent();
	ENGINE_API UClass* Z_Construct_UClass_UActorComponent();
	UPackage* Z_Construct_UPackage__Script_Collage3D_V3();
// End Cross Module References
	void UActorSpinComponent::StaticRegisterNativesUActorSpinComponent()
	{
	}
	UClass* Z_Construct_UClass_UActorSpinComponent_NoRegister()
	{
		return UActorSpinComponent::StaticClass();
	}
	struct Z_Construct_UClass_UActorSpinComponent_Statics
	{
		static UObject* (*const DependentSingletons[])();
#if WITH_METADATA
		static const UE4CodeGen_Private::FMetaDataPairParam Class_MetaDataParams[];
#endif
#if WITH_METADATA
		static const UE4CodeGen_Private::FMetaDataPairParam NewProp_PitchValue_MetaData[];
#endif
		static const UE4CodeGen_Private::FFloatPropertyParams NewProp_PitchValue;
#if WITH_METADATA
		static const UE4CodeGen_Private::FMetaDataPairParam NewProp_YawValue_MetaData[];
#endif
		static const UE4CodeGen_Private::FFloatPropertyParams NewProp_YawValue;
#if WITH_METADATA
		static const UE4CodeGen_Private::FMetaDataPairParam NewProp_RollValue_MetaData[];
#endif
		static const UE4CodeGen_Private::FFloatPropertyParams NewProp_RollValue;
		static const UE4CodeGen_Private::FPropertyParamsBase* const PropPointers[];
		static const FCppClassTypeInfoStatic StaticCppClassTypeInfo;
		static const UE4CodeGen_Private::FClassParams ClassParams;
	};
	UObject* (*const Z_Construct_UClass_UActorSpinComponent_Statics::DependentSingletons[])() = {
		(UObject* (*)())Z_Construct_UClass_UActorComponent,
		(UObject* (*)())Z_Construct_UPackage__Script_Collage3D_V3,
	};
#if WITH_METADATA
	const UE4CodeGen_Private::FMetaDataPairParam Z_Construct_UClass_UActorSpinComponent_Statics::Class_MetaDataParams[] = {
		{ "BlueprintSpawnableComponent", "" },
		{ "ClassGroupNames", "Custom" },
		{ "IncludePath", "ActorSpinComponent.h" },
		{ "ModuleRelativePath", "ActorSpinComponent.h" },
	};
#endif
#if WITH_METADATA
	const UE4CodeGen_Private::FMetaDataPairParam Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_PitchValue_MetaData[] = {
		{ "Category", "ActorSpinComponent" },
		{ "ModuleRelativePath", "ActorSpinComponent.h" },
	};
#endif
	const UE4CodeGen_Private::FFloatPropertyParams Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_PitchValue = { "PitchValue", nullptr, (EPropertyFlags)0x0010000000000001, UE4CodeGen_Private::EPropertyGenFlags::Float, RF_Public|RF_Transient|RF_MarkAsNative, 1, STRUCT_OFFSET(UActorSpinComponent, PitchValue), METADATA_PARAMS(Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_PitchValue_MetaData, UE_ARRAY_COUNT(Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_PitchValue_MetaData)) };
#if WITH_METADATA
	const UE4CodeGen_Private::FMetaDataPairParam Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_YawValue_MetaData[] = {
		{ "Category", "ActorSpinComponent" },
		{ "ModuleRelativePath", "ActorSpinComponent.h" },
	};
#endif
	const UE4CodeGen_Private::FFloatPropertyParams Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_YawValue = { "YawValue", nullptr, (EPropertyFlags)0x0010000000000001, UE4CodeGen_Private::EPropertyGenFlags::Float, RF_Public|RF_Transient|RF_MarkAsNative, 1, STRUCT_OFFSET(UActorSpinComponent, YawValue), METADATA_PARAMS(Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_YawValue_MetaData, UE_ARRAY_COUNT(Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_YawValue_MetaData)) };
#if WITH_METADATA
	const UE4CodeGen_Private::FMetaDataPairParam Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_RollValue_MetaData[] = {
		{ "Category", "ActorSpinComponent" },
		{ "ModuleRelativePath", "ActorSpinComponent.h" },
	};
#endif
	const UE4CodeGen_Private::FFloatPropertyParams Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_RollValue = { "RollValue", nullptr, (EPropertyFlags)0x0010000000000001, UE4CodeGen_Private::EPropertyGenFlags::Float, RF_Public|RF_Transient|RF_MarkAsNative, 1, STRUCT_OFFSET(UActorSpinComponent, RollValue), METADATA_PARAMS(Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_RollValue_MetaData, UE_ARRAY_COUNT(Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_RollValue_MetaData)) };
	const UE4CodeGen_Private::FPropertyParamsBase* const Z_Construct_UClass_UActorSpinComponent_Statics::PropPointers[] = {
		(const UE4CodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_PitchValue,
		(const UE4CodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_YawValue,
		(const UE4CodeGen_Private::FPropertyParamsBase*)&Z_Construct_UClass_UActorSpinComponent_Statics::NewProp_RollValue,
	};
	const FCppClassTypeInfoStatic Z_Construct_UClass_UActorSpinComponent_Statics::StaticCppClassTypeInfo = {
		TCppClassTypeTraits<UActorSpinComponent>::IsAbstract,
	};
	const UE4CodeGen_Private::FClassParams Z_Construct_UClass_UActorSpinComponent_Statics::ClassParams = {
		&UActorSpinComponent::StaticClass,
		"Engine",
		&StaticCppClassTypeInfo,
		DependentSingletons,
		nullptr,
		Z_Construct_UClass_UActorSpinComponent_Statics::PropPointers,
		nullptr,
		UE_ARRAY_COUNT(DependentSingletons),
		0,
		UE_ARRAY_COUNT(Z_Construct_UClass_UActorSpinComponent_Statics::PropPointers),
		0,
		0x00B000A4u,
		METADATA_PARAMS(Z_Construct_UClass_UActorSpinComponent_Statics::Class_MetaDataParams, UE_ARRAY_COUNT(Z_Construct_UClass_UActorSpinComponent_Statics::Class_MetaDataParams))
	};
	UClass* Z_Construct_UClass_UActorSpinComponent()
	{
		static UClass* OuterClass = nullptr;
		if (!OuterClass)
		{
			UE4CodeGen_Private::ConstructUClass(OuterClass, Z_Construct_UClass_UActorSpinComponent_Statics::ClassParams);
		}
		return OuterClass;
	}
	IMPLEMENT_CLASS(UActorSpinComponent, 3176646676);
	template<> COLLAGE3D_V3_API UClass* StaticClass<UActorSpinComponent>()
	{
		return UActorSpinComponent::StaticClass();
	}
	static FCompiledInDefer Z_CompiledInDefer_UClass_UActorSpinComponent(Z_Construct_UClass_UActorSpinComponent, &UActorSpinComponent::StaticClass, TEXT("/Script/Collage3D_V3"), TEXT("UActorSpinComponent"), false, nullptr, nullptr, nullptr);
	DEFINE_VTABLE_PTR_HELPER_CTOR(UActorSpinComponent);
PRAGMA_ENABLE_DEPRECATION_WARNINGS
#ifdef _MSC_VER
#pragma warning (pop)
#endif
